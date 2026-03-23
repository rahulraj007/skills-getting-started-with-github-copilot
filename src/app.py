"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball": {
        "description": "Learn basketball skills and compete in friendly matches",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu"]
    },
    "Soccer": {
        "description": "Practice soccer techniques and play recreational games",
        "schedule": "Tuesdays and Thursdays, 3:45 PM - 5:15 PM",
        "max_participants": 20,
        "participants": ["lucas@mergington.edu", "sophie@mergington.edu"]
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and other visual arts",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["isabella@mergington.edu"]
    },
    "Music Band": {
        "description": "Learn instruments and perform in school concerts",
        "schedule": "Mondays and Fridays, 3:30 PM - 4:45 PM",
        "max_participants": 25,
        "participants": ["david@mergington.edu", "grace@mergington.edu"]
    },
    "Debate Club": {
        "description": "Develop public speaking and critical thinking skills through debates",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": ["alex@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore STEM concepts through hands-on projects",
        "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["ryan@mergington.edu", "mia@mergington.edu"]
    },
    "Tennis": {
        "description": "Learn tennis skills and compete in friendly matches",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["noah@mergington.edu"]
    },
    "Volleyball": {
        "description": "Develop volleyball techniques and participate in team games",
        "schedule": "Wednesdays and Fridays, 3:45 PM - 5:15 PM",
        "max_participants": 18,
        "participants": ["ava@mergington.edu", "liam@mergington.edu"]
    },
    "Theater": {
        "description": "Act in school plays and learn stagecraft and performance skills",
        "schedule": "Tuesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["charlotte@mergington.edu", "benjamin@mergington.edu"]
    },
    "Photography": {
        "description": "Learn photography techniques and digital image editing",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 14,
        "participants": ["amelia@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and prepare for math competitions",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["harper@mergington.edu", "mason@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Build and program robots to compete in robotics competitions",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ethan@mergington.edu", "scarlett@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Check if student is already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
