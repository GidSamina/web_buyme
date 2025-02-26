pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // This checks out the code from the repository.
                git(url: 'https://github.com/GidSamina/web_buyme.git', branch: 'main')
            }
        }
        stage('Run Script') {
            steps {
                    echo "Running myapp.py on main branch..."
                    bat "python C://Users/97252/PycharmProjects/PythonProject1/PythonProject/web_buyme/BuyMe_new.py"

                }
            }
        }

}