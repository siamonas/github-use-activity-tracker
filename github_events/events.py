from rich import print

def print_commit_comment_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :memo: Commented on a commit in {repo_name}")

def print_create_event(event):
    repo_name = event["repo"]["name"]
    ref_type = event["payload"]["ref_type"]
    print(f"- :sparkles: Created a {ref_type} in {repo_name}")

def print_delete_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :wastebasket: Deleted a branch or tag in {repo_name}")

def print_fork_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :fork_and_knife: Forked {repo_name}")

def print_gollum_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :book: Updated the wiki in {repo_name}")

def print_issue_comment_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :left_speech_bubble: Commented on an issue in {repo_name}")

def print_issues_event(event):
    repo_name = event["repo"]["name"]
    action = event["payload"]["action"]
    print(f"- :closed_umbrella: {action.capitalize()} an issue in {repo_name}")

def print_member_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :busts_in_silhouette: Added a member to {repo_name}")

def print_public_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :globe_with_meridians: Made {repo_name} public")

def print_pull_request_event(event):
    repo_name = event["repo"]["name"]
    action = event["payload"]["action"]
    print(f"- :arrows_counterclockwise: {action.capitalize()} a pull request in {repo_name}")

def print_pull_request_review_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :mag: Reviewed a pull request in {repo_name}")

def print_pull_request_review_comment_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :left_speech_bubble: Commented on a pull request review in {repo_name}")

def print_push_event(event):
    repo_name = event["repo"]["name"]
    commits = len(event["payload"]["commits"])
    print(f"- :arrow_up_small: Pushed {commits} commit(s) to {repo_name}")

def print_release_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :package: Released a new version in {repo_name}")

def print_sponsorship_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :moneybag: Sponsored {repo_name}")

def print_watch_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :star: Starred {repo_name}")

def print_unknown_event(event):
    repo_name = event["repo"]["name"]
    print(f"- :question: Performed an unknown action in {repo_name}")

def print_event_details(event):
    type = event["type"]    
    match type:
        case "CommitCommentEvent":
            print_commit_comment_event(event)
        case "CreateEvent":
            print_create_event(event)
        case "DeleteEvent":
            print_delete_event(event)
        case "ForkEvent":
            print_fork_event(event)
        case "GollumEvent":
            print_gollum_event(event)
        case "IssueCommentEvent":
            print_issue_comment_event(event)
        case "IssuesEvent":
            print_issues_event(event)
        case "MemberEvent":
            print_member_event(event)
        case "PublicEvent":
            print_public_event(event)
        case "PullRequestEvent":
            print_pull_request_event(event)
        case "PullRequestReviewEvent":
            print_pull_request_review_event(event)
        case "PullRequestReviewCommentEvent":
            print_pull_request_review_comment_event(event)
        #case "PullRequestReviewThreadEvent":
        #   print_pull_request_review_thread_event(event)
        case "PushEvent":
            print_push_event(event)
        case "ReleaseEvent":
            print_release_event(event)
        case "SponsorshipEvent":
            print_sponsorship_event(event)
        case "WatchEvent":
            print_watch_event(event)
        case _:
            print_unknown_event(event)