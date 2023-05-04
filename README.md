
# Waist Size Measurer

Waist Size Measurer is an application where you can input your height, weight & age it will give you the value of your waist size. You can also add your waist size if that is not present in the database.
Start the backend uvicorn server first then start the react server.




## Screenshots

![Fastapi Api's Screenshot](https://drive.google.com/file/d/1A_Wr8zeWjkQLrSesYCHamKQVlDjMJx5i/view?usp=sharing)

https://drive.google.com/file/d/1A_Wr8zeWjkQLrSesYCHamKQVlDjMJx5i/view?usp=sharing

## Run Backend FastAPI Locally


Clone the project

```bash
  git clone https://github.com/yuvi-1701/FullStackApp.git
```

Go to the project directory

```bash
  cd FullStackApp/backend
```

Install dependencies

```bash
  cd .. 
  py -m venv myenv  ->(optional)
  ./myenv/Scripts/Activate.ps1   ->(For windows machine to activate virtual environment in powershell)
  cd backend
  pip install -r requirements.txt
```

Start the server

```bash
  (after installing all dependencies run below cmd. It will run fastapi server on 8000 port by default to open it on different port add {--port portnumber} at the back of the below cmd.)
  uvicorn myapp.app:app --reload 
```

Now What?

```bash
  Now you can click on the link provided by fast api like (http://127.0.0.1:8000) and then to check it on the swagger ui you can hit http://127.0.0.1:8000/docs. Here you can test our endpoints as shown in the screenshot above. As Backend is now running you can follow below steps to run frontend as well
 ```


## Run Frontend React Locally

Clone the project

```bash
  (Optional if already done then dont do it.)
  git clone https://github.com/yuvi-1701/FullStackApp.git 
```

Go to the project directory

```bash
  cd FullStackApp/frontend/my-app
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```

## Authors

- [@YuvrajDarekar](https://www.github.com/yuvi-1701)
