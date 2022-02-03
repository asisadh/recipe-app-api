build docker: docker build .
build docker-compose: docker-compose build
//run project: docker-compose run app sh -c "django-admin.py startproject app ."
run project: docker-compose run app sh -c "python -m django startproject app ."
