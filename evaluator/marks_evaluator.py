from sentence_transformers import SentenceTransformer, util
import spacy
import language_tool_python
import re
from pmongo import MongoClient

client = MongoClient("mongodb+srv://sidwebdsingh04:FRtzqHoy5ERBUhyB@cluster0.df0agi3.mongodb.net/") #url for mongodb database
db = client["test"]
questions_collection = db["subjectivequestions"]

nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer('all-MiniLM-L6-v2')
tool = language_tool_python.LanguageTool('en-US')

def semantic_similarity(student_ans, reference_ans):
    student_ans_emb = model.encode(student_ans, convert_to_tensor=True)
    reference_ans_emb = model.encode(reference_ans, convert_to_tensor=True)
    sim = util.pytorch_cos_sim(student_ans_emb, reference_ans_emb).item()
    return sim

def keyword_coverage(student_ans, reference_ans):
    doc_ref = nlp(reference_ans.lower())
    doc_stu = nlp(student_ans.lower())
    ref_keywords = {token.lemma_ for token in doc_ref if token.pos_ in ["NOUN", "VERB", "ADJ"]}
    stu_keywords = {token.lemma_ for token in doc_stu if token.pos_ in ["NOUN", "VERB", "ADJ"]}

    if not ref_keywords:
        return 1.0
    matched = len(ref_keywords.intersection(stu_keywords))
    return matched / len(ref_keywords)

def grammar_score(student_ans):
    matches = tool.check(student_ans)
    errors = len(matches)
    words = len(re.findall(r'\w+', student_ans))
    if words == 0:
        return 0.0
    error_rate = errors / words
    if error_rate <= 0.02:
        return 1.0
    elif error_rate <= 0.05:
        return 0.7
    else:
        return 0.4

def evaluate_answer(student_ans, reference_ans, max_marks=10):
    sim = semantic_similarity(student_ans, reference_ans)
    key = keyword_coverage(student_ans, reference_ans)
    gram = grammar_score(student_ans)
    final_score = (0.6 * sim + 0.3 * key + 0.1 * gram) * max_marks
    return round(final_score, 2)

def check_answer(question_id, student_ans, student_id="S1"):
    # Fetch reference answer from MongoDB
    question = questions_collection.find_one({"_id": question_id})
    if not question:
        return {"error": "Question not found"}

    reference_ans = question["answerText"]
    max_marks = question.get("marks", 10)

    # Run evaluation
    score = evaluate_answer(student_ans, reference_ans, max_marks)

    # Optionally save student result back to DB
    db["student_answers"].insert_one({
        "questionId": question_id,
        "studentId": student_id,
        "studentAnswer": student_ans,
        "score": score
    })

    return {
        "question": question["questionText"],
        "referenceAnswer": reference_ans,
        "studentAnswer": student_ans,
        "score": score
    }

if __name__ == "__main__":
    # Example: pass ObjectId of question from MongoDB
    from bson import ObjectId
    qid = ObjectId("68a76d44b1f0f179d46a1e0a")  # replace with actual _id from DB
    student_answer = "answer is 7"
    result = check_answer(qid, student_answer, student_id="STU101")
    print(result)