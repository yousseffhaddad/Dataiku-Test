# **C3PO Program: Odds Computation for the Millennium Falcon**

The purpose of this repository is to implement a C3PO program that computes the odds of the Millennium Falcon reaching Endor in time to save the galaxy.

---

## **Features**
- **DDD Architecture**  
  The project is built following the principles of Domain-Driven Design (DDD), ensuring clean and modular code.
  
- **Dependency Injection Implementation**  
  Abstract classes and services are registered using the `dependency_injector` library, promoting testability and separation of concerns.

- **Logs Saving**  
  Comprehensive logging implemented for debugging and monitoring, with logs stored in easily accessible files.

- **Environment Variable Configuration**  
  File paths and other configurations can be customized through an `.env` file, providing flexibility without code changes.

- **Exception Handling**  
  Robust custom exception classes ensure meaningful error messages and graceful error handling.

---

## **Getting Started**
### **Requirements**
- Python 3.9 or later  
- Dependencies listed in [requirements.txt](src/requirements.txt)

### **Setup**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd Dataiku - technicalTest/src
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Configure paths of the json files in the src/config/app.env file:
   ```bash
   MILLENNIUM_FALCON_FILE_PATH=src/assets/examples/example4/millennium-falcon.json
   EMPIRE_JSON_FILE_PATH=src/assets/examples/example4/empire.json
   
5. Run main.py script:
   ```bash
   python3 main.py 

