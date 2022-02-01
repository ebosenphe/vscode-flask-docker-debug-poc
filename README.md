## Original article
[Flask Debugging in VS Code with Hot-Reload 🔥](https://blog.theodo.com/2020/05/debug-flask-vscode/)


https://github.com/adriencaccia/vscode-flask-debug

## 🔧 Prerequisites

- **VS Code**
- **Docker**
- **Docker Compose**
- The [**VS Code Python extension**](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## 🎉 Getting Started

- Install the requirements
    ```bash
    make install
    ```
- Run the app with `make` command :
  - Using `flask` runner
    - Server with Hot-Reloading
      ```bash
      make flask
      ```
    - Server with Debugger and Hot-Reloading
      ```bash
      make flaskdebug
      ```
  - Using `gunicorn` runner
    - Server with Hot-Reloading
      ```bash
      make gunicorn
      ```
    - Server with Debugger and Hot-Reloading
      ```bash
      make gunicorndebug
      ```
- Run the app with `VSCode Tasks`

    ```bash
    Press simultaniously CTRL + ALT + T and you will get a popup widow were you can choose your option 
    ```
    ![VSCode Task Options](/assets/png/vsCodeTasksOptions.PNG)

## Further notes

    Exception is thrown during 
    ```bash
    make flaskdebug
    ```

    To avoid this, make sure that you uncheck Uncaught Exceptions as it will crash the debugger when hot reloading the code after a change.
    This is possibly a bug in debugpy
    
    ![VSCode Debugger Options](/assets/png/debugger.PNG)
