from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import json

ISSUES_FILE = 'C:\Users\DivyaRanganathan\Desktop\airtribe\Learning\devtrack\devtrack\issues.json'
REPORTERS_FILE = 'C:\Users\DivyaRanganathan\Desktop\airtribe\Learning\devtrack\devtrack\reporters.json'

@api_view(['GET'])
def get_reporters(request: Request):
    reporter_id = request.GET.get('id')
    with open(REPORTERS_FILE, 'r') as f:
        reporters = json.load(f)
    if reporter_id:
        reporter_id = int(reporter_id)
        for reporter in reporters:
            if reporter['id'] == reporter_id:
                return Response(reporter, status=200)
    return Response(reporters)

@api_view(['GET'])
def get_issues(request: Request):
    issue_id = request.GET.get('id')
    status_value = request.GET.get('status')

    with open(ISSUES_FILE, 'r') as f:
        issues = json.load(f)

    # If ID is provided → return single issue
    if issue_id:
        issue_id = int(issue_id)
        for issue in issues:
            if issue['id'] == issue_id:
                return Response(issue, status=200)
        return Response({'error': 'Issue not found'}, status=404)

    # If status is provided → filter issues
    if status_value:
        filtered_issues = [
            issue for issue in issues
            if issue.get('status', '').lower() == status_value.lower()
        ]
        return Response(filtered_issues, status=200)

    # Otherwise → return all issues
    return Response(issues, status=200)

@api_view(['POST'])
def create_reporter(request):
    # Read from Request
    data = json.loads(request.body)

    # Open the file
    with open(REPORTERS_FILE, 'r') as f:
        reporters = json.load(f)

    # Create new reporter
    new_reporter ={
        "id": data["id"],
        "name": data["name"],
        "email": data["email"],
        "team": data["team"],
    }
    
    # Append the new reporter
    reporters.append(new_reporter)

    # Write the file
    with open(REPORTERS_FILE, 'w') as f:
        json.dump(reporters, f, indent=2)

    return Response(new_reporter)

    
@api_view(['POST'])
def create_issue(request):
    # Read from Request
    data = json.loads(request.body)

    # Open the file
    with open(ISSUES_FILE, 'r') as f:
        issues = json.load(f)

    # Create new reporter
    new_issue ={
        "id": data["id"],
        "title": data["title"],
        "description": data["description"],
        "status": data["status"],
        "priority": data["priority"],
        "reporter_id": data["reporter_id"],
    }
    
    # Append the new reporter
    issues.append(new_issue)

    # Write the file
    with open(REPORTERS_FILE, 'w') as f:
        json.dump(issues, f, indent=2)

    return Response(new_issue)