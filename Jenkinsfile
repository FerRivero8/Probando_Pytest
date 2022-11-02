pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('Pytest') {
      steps {
        bat 'pytest -v prueba_test.py'
      }
    }
  }
}
