pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python3 --version'
      }
    }
    stage('pip') {
      steps {
        bat 'pip list'
      }
    }
  }
}
