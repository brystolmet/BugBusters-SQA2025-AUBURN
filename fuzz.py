import random
import string
import myLogger
import exampleConstants

#from parser.py
def checkIfWeirdYAML(yaml_script):
    '''
    to filter invalid YAMLs such as ./github/workflows/
    '''
    val = False
    if ( any(x_ in yaml_script for x_ in exampleConstants.WEIRD_PATHS  ) ):
        val = True
        logObj.info(f"{yaml_script} is weird")
    return val

#from parser.py
def readYAMLAsStr( path_script ):
    yaml_as_str = exampleConstants.YAML_SKIPPING_TEXT
    with open( path_script , exampleConstants.FILE_READ_FLAG) as file_:
        yaml_as_str = file_.read()
        logObj.info(f"YAML content read: {path_script}")
    return yaml_as_str

#from parser.py
def checkIfValidHelm(path_script):
    val_ret = False
    if ( (exampleConstants.HELM_KW in path_script) or (exampleConstants.CHART_KW in path_script) or (exampleConstants.SERVICE_KW in path_script) or (exampleConstants.INGRESS_KW in path_script)  or(exampleConstants.HELM_DEPLOY_KW in path_script) or (exampleConstants.CONFIG_KW in path_script) )  and (exampleConstants.VALUE_KW in path_script) :
        val_ret = True
        logObj.info(f"Valid Helm: {path_script}")
    return val_ret

#from scanner.py
def isValidUserName(uName):
    valid = True
    if (isinstance( uName , str)  ):
        if( any(z_ in uName for z_ in exampleConstants.FORBIDDEN_USER_NAMES )   ):
            valid = False
            logObj.info(f"Forbidden username: {uName}")
        else:
            valid = True
    else:
        valid = False
    return valid

#from scanner.py
def isValidPasswordName(pName):
    valid = True
    if (isinstance( pName , str)  ):
        if( any(z_ in pName for z_ in exampleConstants.FORBIDDEN_PASS_NAMES) )  :
            valid = False
            logObj.info(f"Forbidden password: {pName}")
        else:
            valid = True
    else:
        valid = False
    return valid


def fuzzValues(x):
    pyMethods = [
        "checkIfWeirdYAML",
        "readYAMLAsStr",
        "checkIfValidHelm",
        "isValidUserName",
        "isValidPasswordName"
    ]

    for method in pyMethods:
        try:
            logObj.info(f"Running {method} on {x}")
            result = globals()[method](x)
            print(result)
            logObj.info(f"Result of {method}: {result}")
        except Exception as e:
            error_msg = f"Crash Caught in {method}: {str(e)}"
            print(error_msg)
            logObj.error(error_msg)


def simpleFuzzer():
    yaml = "exampleEnvironment.yml"

    try:
        logObj.info(f"Running checkIfWeirdYAML on {yaml}")
        result = checkIfWeirdYAML(yaml)
        print(f"checkIfWeirdYAML: {result}")
        logObj.info(f"Result of checkIfWeirdYAML: {result}")
    except Exception as e:
        logObj.error(f"Crash in checkIfWeirdYAML: {e}")

    try:
        logObj.info(f"Running readYAMLAsStr on {yaml}")
        result = readYAMLAsStr(yaml)
        print(f"readYAMLAsStr output:\n{result}")
        logObj.info("readYAMLAsStr completed")
    except Exception as e:
        logObj.error(f"Crash in readYAMLAsStr: {e}")

    try:
        logObj.info(f"Running checkIfValidHelm on {yaml}")
        result = checkIfValidHelm(yaml)
        print(f"checkIfValidHelm: {result}")
        logObj.info(f"Result of checkIfValidHelm: {result}")
    except Exception as e:
        logObj.error(f"Crash in checkIfValidHelm: {e}")

    try:
        logObj.info("Testing isValidUserName with input 'domain'")
        result = isValidUserName("domain")
        print(f"isValidUserName('domain'): {result}")
        logObj.info(f"isValidUserName result: {result}")
        logObj.info("Testing isValidUserName with input 'test'")
        result2 = isValidUserName("test")
        print(f"isValidUserName('test'): {result2}")
        logObj.info(f"isValidUserName result: {result2}")
    except Exception as e:
        logObj.error(f"Error in isValidUserName: {e}")

    try:
        logObj.info("Testing isValidPasswordName with input '_auth'")
        result = isValidPasswordName("_auth")
        print(f"isValidPasswordName('_auth'): {result}")
        logObj.info(f"isValidPasswordName result: {result}")
        logObj.info("Testing isValidUserName with input 'test'")
        result2 = isValidPasswordName("test")
        print(f"isValidPasswordName('test'): {result2}")
        logObj.info(f"isValidPasswordName result: {result2}")
    except Exception as e:
        logObj.error(f"Error in isValidPasswordName: {e}")


if __name__=='__main__':
    logObj = myLogger.giveMeLoggingObject()
    logObj.info("This is the start of the project logging")
    simpleFuzzer()
