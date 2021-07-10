# KVISOI
A simple web application that judges codes, made for KVIS Olympiad in Informatics Club.
## Instruction 
### To run the program
  1. download **JUST** the deploy_env directory 
  2. edit the docker-compose.yml file. correct the site configuration.
  4. deploy using `docker-compose up`
  5. run `python manage.py makemigrations` and `python manage.py migrate` in the docker shell (if needed)
### To add Tasks
  1. access the admin page and add new task object
  2. upload the task input and output to the /grader_config/tasks/<task_id>
  3. don't forget the manifest.json
### To access admin page
  1. create new superuser by `python manage.py createsuperuser`
  2. access /admin and login
### To contribute
  1. Fork this project and make a PR!

## Concerns
### API route is not blocked
  - Anyone can send request to certain endpoint to fake judge result
  - to be fix by restricting those endpoints from external access
    - Traefik can handle this (waiting for the next update for a neat implementation)

## Things to be improved
- Templates obviously (responsive will be appreciated)
- Use websocket to update submission
- Write tests
- Table pagination and search
- Ability to rejudge (for admin)
- Contest management ?
- Better profile page
- Some kind of automation in adding a task
- Add subission timestamp (cause why not)
