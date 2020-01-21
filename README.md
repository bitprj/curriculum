# Developer Relations Workflow
## Stage 1 - Prereview
Step 1: Create a Branch named firstname_activityorlabname
Step 2: When you are done commiting and ready for your reviewer to review change
- Stage to "Pending Reviewer"
- Assign the merge request to your reviewer
- Reference the Issue you are working on in your MERGE REQUEST!

## Stage Overview

Stage 1 (Pre-Review): DevRel Stage 1
Stage 2 (Post-Review): Continue Perfecting DevRel Stage 1 + DevRel Stage 2
Stage 3 (Kevin): Kevin conducts final review
Stage 4 (Writers): Writers re-style curriculum for grammar, writing style etc.
Stage 5 (Contentful): Writers copy and paste into Contentful

Additionally, Stages 1-3 are handled and marked within GitLab.

Stage 4 is the GitLab issue that Kevin will raise.

Stage 5 is Contentful.

## Stage Processes

Bullet points indicate steps to be completed, when all the bullet points are done in order, then the corresponding status for that stage should be marked in Airtable. 

### Stage 1: Before 1st Review

* Reviewers (complete before developer starts merge request)
  * Start GitLab merge requests pertaining to each activity/lab
* Developers
  * Assigned a specific folder to work in 
  * Develop curriculum by DevRel Stage 1 Requirements
  * Devs upload folder of .md files to the folder assigned 
  * Start **merge request** and assign to reviewer 
  * Mark "Pre-Review" stage in GitLab "label"

> Note that Stages 2-4 are completed **in the same merge request!**

### Aside on Comments (Stages 2-4)

* Developers: For every single commit to a merge request, please put "/spend xx hours".
  * We would like to get a good idea of your work to place you in the right team

### Stage 2: After 1st Review 

* Reviewer reviews .md files
  * Leave feedback in terms of **comments** on merge request
  * Reviewer leaves comments
    * Types of issues
      * Context (explanations of underlying concepts)
      * Content (code and explanations of code)
      * Styling (separating cards into steps, typos, flow, only local images)
      * Visuals (custom visuals)
      * Create (need to create a new card)
    * **Resolve all comments into an issue**
* Developer responds to comments
  * By going to issue 
* Developer + reviewer work together to get all comment threads resolved
* Reviewer changes assignee to Kevin
* Mark "Post-Review" in GitLab "label"

### Stage 3: Final Review 

* Kevin conducts one final review, makes comments where necessary
* Kevin works with reviewer and developers to resolve comments
* When all comments resolved, Kevin updates GitLab status to "Final Review"   

### Stage 4: Technical Writers 

* Kevin raises an issue and changes assignee to writer 
  * Writer will re-style curriculum
* When finished, writers mark status to "Final Edits"

### Stage 5: Contentful

* Writers copy and paste into Contentful, format accordingly
* Writers finish, publish within Contentful 



