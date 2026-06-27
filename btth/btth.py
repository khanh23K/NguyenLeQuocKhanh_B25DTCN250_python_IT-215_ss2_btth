from fastapi import FastAPI

app = FastAPI()

courses = [
    {
        "id": 1,
        "code": "PY101",
        "name": "Python Basic",
        "level": "beginner",
        "price": 1500000
    },
    {
        "id": 2,
        "code": "FA101",
        "name": "FastAPI Basic",
        "level": "beginner",
        "price": 2000000
    },
    {
        "id": 3,
        "code": "JS102",
        "name": "JavaScript Advanced",
        "level": "intermediate",
        "price": 2500000
    }
]
@app.get("/health")
def check_health():
    return {"message": "API is running"}

@app.get("/courses")
def get_all_courses():
    return courses
@app.get("/courses/{course_id}")
def get_course_detail(course_id: int):
    if course_id <= 0:
        return {
            "status": "error",
            "message": "ID khóa học không hợp lệ. ID phải lớn hơn 0."
        }
    for course in courses:
        if course["id"] == course_id:
            return {
                "status": "success",
                "data": course
            }
    return {
        "status": "error",
        "message": f"Không tìm thấy khóa học nào có ID bằng {course_id}."
    }