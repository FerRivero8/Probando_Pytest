pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('pip') {
      steps {
        bat 'pip list'
      }
    }
    stage('Pytest Version') {
      steps {
        bat 'pytest --version'
      }
    }
  }
}
