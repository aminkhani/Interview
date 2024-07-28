# Interview Project
    
## How run the project?

1) Edit **`.env.sample`** and add your configuration & change the file name to **`.env`**.
2) Run **`docker compose up --build`**.
3) Connect to the container: **`docker exec -it phone_registration-web-1 bash`** (set your container name)
4) In the container: **`python manage.py createsuperuser`** (create super user for login)
5) Search in browser: [**`localhost:8080`**](http://localhost:8000)

### Connect to database

- Host: **`localhost`**
- User: **`<username>`**
- Password: **`<password>`**
- Database: **`<database>`**
- Port: **`5431`**

## End-points

- Home: [**`localhost:8000/`**](http://localhost:8000/)
- Admin Panel: [**`localhost:8000/admin`**](http://localhost:8000/admin)
- Phones List: [**`localhost:8000/phones/`**](http://localhost:8000/phones/)
- Add Phone: [**`localhost:8000/add-phone/`**](http://localhost:8000/add-phone/)
- Add Phone: [**`localhost:8000/get-report/`**](http://localhost:8000/get-report/)

## Improvements

- Working on front-end for better viewing
- Writing script to add dummy data
- Working on admin panel ui
- Working on get report end-point

## Challenges

-Design Database (ERD)
  - See ERD folder 

### Time to complete

- It approximately takes 6 hours.

### Difficulty

- Simple
