import time

def check_my_environment():
    '''
    This function tests to see if you can import arcpy and arcgis.
    If you can, it tells you so.  If not, it will tell you to check your environment
    '''
    try:
        import arcgis
        import arcpy
        print('You did it!  You got the right environment')
        time.sleep(20)
        print('Goodbye')
    except:
        print('You probably got the wrong environment')
        time.sleep(20)

        
# This only executes if you double-click the script or run this script
if __name__ == '__main__':
    print('STARTING YOUR JOB')
    check_my_environment()