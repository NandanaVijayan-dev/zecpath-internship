import json
import os

FILE_NAME = "candidates.json"

def init_db():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            json.dump([], file) 

def read_data():
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def write_data(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

def create_candidate(name, role):
    data = read_data()
    new_id = len(data) + 1
    new_candidate = {"id": new_id, "name": name, "role": role}
    data.append(new_candidate)
    write_data(data)
    print(f"Created: {name}")

def get_candidates():
    data = read_data()
    print("--- Candidate List ---")
    for c in data:
        print(f"[{c['id']}] {c['name']} - {c['role']}")

def update_candidate(candidate_id, new_role):
    data = read_data()
    for c in data:
        if c['id'] == candidate_id:
            c['role'] = new_role
            write_data(data)
            print(f"Updated candidate {candidate_id} to {new_role}")
            return
    print(f"Candidate {candidate_id} not found.")

def delete_candidate(candidate_id):
    data = read_data()
    filtered_data = [c for c in data if c['id'] != candidate_id]
    write_data(filtered_data)
    print(f"Deleted candidate {candidate_id}")

print("Starting CRUD Simulation...\n")
init_db()
create_candidate("Alice", "Frontend Developer")
create_candidate("Bob", "Backend Developer")
get_candidates()
update_candidate(1, "Full Stack Developer")
get_candidates()
delete_candidate(2)
get_candidates()