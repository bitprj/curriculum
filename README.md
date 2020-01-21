# Developer Relations Workflow
##Stage 1 - Prereview
Step 1: Create a Branch named firstname_activityorlabname
Step 2: When you are done commiting and ready for your reviewer to review change
- Stage to "Pending Reviewer"
- Assign the merge request to your reviewer
- Reference the Issue you are working on in your MERGE REQUEST!

## Stage Overview

Stage 1 (Pre-Review): DevRel Stage 1
Stage 2 (Post-Review): Continue Perfecting DevRel Stage 1 + DevRel Stage 2
Stage 3 (Kevin): Kevin conducts final review

ghjkjh
Stage 4 (Writers): Writers re-style curriculum for grammar, writing style etc.
Stage 5 (Contentful): Writers copy and paste into Contentful

Additionally, Stages 1-3 are handled and marked within GitLab.

Stage 4 is the GitLab issue that Kevin will raise.

Stage 5 is Contentful.

## Stage Processes

Developers are assigned a specific folder to work in -> Devs upload folder of .md files to the folder assigned (in Stage 1) -> start merge request and assign to reviewer (mark Stage 1) -> 

---

(note the steps within these lines are within the merge request)
reviewer reviews the .md files and comment on merge
request accordingly (in Stage 2) -> reviewer has all comment threads resolved (mark Stage 2) -> 
reviewer changes assignee to Kevin (in Stage 3) -> Kevin conducts one final review, makes comments where necessary (in stage 3) -> when all comments resolved, Kevin resolves merge request (mark Stage 3) 

---

-> Kevin raises an issue and assigns writers to re-style (in Stage 4) -> writers re-style and start new merge request that closes issue automatically (https://docs.gitlab.com/ee/user/project/issues/managing_issues.html) (mark Stage 4) -> Writers copy and paste into Contentful, format accordingly (in Stage 5) -> Writers finish, publish within Contentful (mark Stage 5, done!) 

## Airtable's Role

Note that stages should be constantly updated on Airtable. 

"Mark stage x" indicates that stage x is done, and it should be *marked* on Airtable.
