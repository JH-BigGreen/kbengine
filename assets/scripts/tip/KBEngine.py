# base成员函数
def addWatcher( path, dataType, getFunction ):  
    """ base成员函数 """
    pass
def address( ):  
    """ base成员函数 """
    pass
def MemoryStream( ):  
    """ base成员函数 """
    pass
def charge( ordersID, dbID, byteDatas, pycallback ):  
    """ base成员函数 """
    pass
def createEntity( ):  
    """ base成员函数 """
    pass
def createEntityAnywhere( entityType, *params, callback ):  
    """ base成员函数 """
    pass
def createEntityRemotely( entityType, baseMB, *params, callback ):  
    """ base成员函数 """
    pass
def createEntityFromDBID( entityType, dbID, callback, dbInterfaceName ):  
    """ base成员函数 """
    pass
def createEntityAnywhereFromDBID( entityType, dbID, callback, dbInterfaceName ):  
    """ base成员函数 """
    pass
def createEntityRemotelyFromDBID( entityType, dbID, baseMB, callback, dbInterfaceName ):  
    """ base成员函数 """
    pass
def createEntityLocally( entityType, *params ):  
    """ base成员函数 """
    pass
def debugTracing( ):  
    """ base成员函数 """
    pass
def delWatcher( path ):  
    """ base成员函数 """
    pass
def deleteEntityByDBID( entityType, dbID, callback, dbInterfaceName ):  
    """ base成员函数 """
    pass
def deregisterReadFileDescriptor( fileDescriptor ):  
    """ base成员函数 """
    pass
def deregisterWriteFileDescriptor( fileDescriptor ):  
    """ base成员函数 """
    pass
def executeRawDatabaseCommand( command, callback, threadID, dbInterfaceName ):      
    """ base成员函数 """
    pass
def genUUID64( ):  
    """ base成员函数 """
    pass
def getResFullPath( res ):  
    """ base成员函数 """
    pass
def getWatcher( path ):  
    """ base成员函数 """
    pass
def getWatcherDir( path ):  
    """ base成员函数 """
    pass
def getAppFlags( ):  
    """ base成员函数 """
    pass
def hasRes( res ):  
    """ base成员函数 """
    pass
def isShuttingDown( ):  
    """ base成员函数 """
    pass
def listPathRes( path, extension ):  
    """ base成员函数 """
    pass
def lookUpEntityByDBID( entityType, dbID, callback, dbInterfaceName ):  
    """ base成员函数 """
    pass
def matchPath( res ):  
    """ base成员函数 """
    pass
def open( res, mode ):  
    """ base成员函数 """
    pass
def publish( ):  
    """ base成员函数 """
    pass
def quantedPercent( ):  
    """ base成员函数 """
    pass
def registerReadFileDescriptor( fileDescriptor, callback ):  
    """ base成员函数 """
    pass
def registerWriteFileDescriptor( fileDescriptor, callback ):  
    """ base成员函数 """
    pass
def reloadScript( fullReload ):  
    """ base成员函数 """
    pass
def scriptLogType( logType ):  
    """ base成员函数 """
    pass
def setAppFlags( flags ):  
    """ base成员函数 """
    pass
def time( ):  
    """ base成员函数 """
    pass
# base回调函数
def onBaseAppReady( isBootstrap ):  
    """ base回调函数 """
    pass
def onBaseAppShutDown( state ):  
    """ base回调函数 """
    pass
def onCellAppDeath( addr ):  
    """ base回调函数 """
    pass
def onFini( ):  
    """ base回调函数 """
    pass
def onBaseAppData( key, value ):  
    """ base回调函数 """
    pass
def onBaseAppDataDel( key ):  
    """ base回调函数 """
    pass
def onLoseChargeCB( orderID, dbID, success, datas ):  
    """ base回调函数 """
    pass
def onReadyForLogin( isBootstrap ):  
    """ base回调函数 """
    pass
def onReadyForShutDown( ):  
    """ base回调函数 """
    pass
def onAutoLoadEntityCreate( entityType, dbID ):  
    """ base回调函数 """
    pass
# cell成员函数
def accelerate( self, accelerateType, acceleration ):  
    """ cell成员函数 """
    pass
def addYawRotator( self, targetYaw, velocity, userArg ):  
    """ cell成员函数 """
    pass
def addProximity( self, range, userArg ):  
    """ cell成员函数 """
    pass
def addTimer( self, start, interval=0.0, userData=0 ):  
    """ cell成员函数 """
    pass
def cancelController( self, controllerID ):  
    """ cell成员函数 """
    pass
def clientEntity( self, destID ):  
    """ cell成员函数 """
    pass
def canNavigate( self ):  
    """ cell成员函数 """
    pass
def debugView( self ):  
    """ cell成员函数 """
    pass
def delTimer( self, id ):  
    """ cell成员函数 """
    pass
def destroy( self ):  
    """ cell成员函数 """
    pass
def destroySpace( self ):  
    """ cell成员函数 """
    pass
def entitiesInView( self ):  
    """ cell成员函数 """
    pass
def entitiesInRange( self, range, entityType=None, position=None ):  
    """ cell成员函数 """
    pass
def isReal( self ):  
    """ cell成员函数 """
    pass
def moveToEntity( self, destEntityID, velocity, distance, userData, faceMovement, moveVertically, offsetPos ):  
    """ cell成员函数 """
    pass
def moveToPoint( self, destination, velocity, distance, userData, faceMovement, moveVertically ):  
    """ cell成员函数 """
    pass
def getViewRadius( self ):  
    """ cell成员函数 """
    pass
def getViewHystArea( self ):  
    """ cell成员函数 """
    pass
def getRandomPoints( self, centerPos, maxRadius, maxPoints, layer ):  
    """ cell成员函数 """
    pass
def navigate( self, destination, velocity, distance, maxMoveDistance, maxSearchDistance, faceMovement, layer, userData ):  
    """ cell成员函数 """
    pass
def navigatePathPoints( self, destination, maxSearchDistance, layer ):  
    """ cell成员函数 """
    pass
def setViewRadius( self, radius, hyst=5 ):  
    """ cell成员函数 """
    pass
def teleport( self, nearbyMBRef, position, direction ):  
    """ cell成员函数 """
    pass
def writeToDB( self, shouldAutoLoad, dbInterfaceName ):  
    """ cell成员函数 """
    pass
# cell回调函数
def onCellAppData( key, value ):  
    """ cell回调函数 """
    pass
def onCellAppDataDel( key ):  
    """ cell回调函数 """
    pass
def onSpaceData( spaceID, key, value ):  
    """ cell回调函数 """
    pass
def onSpaceGeometryLoaded( spaceID, mapping ):  
    """ cell回调函数 """
    pass
def onAllSpaceGeometryLoaded( spaceID, isBootstrap, mapping ):  
    """ cell回调函数 """
    pass
# 共用回调函数
def onGlobalData( key, value ):  
    """ 共用回调函数 """
    pass
def onGlobalDataDel( key ):  
    """ 共用回调函数 """
    pass
def onInit( isReload ):  
    """ 共用回调函数 """
    pass

class Entity:
    #成员函数 
    def addTimer( self, initialOffset, repeatOffset=0, userArg=0 ):  
        """ base成员函数 """
        pass
    def createCellEntity( self, cellEntityMB ):  
        """ base成员函数 """
        pass
    def createCellEntityInNewSpace( self, cellappIndex ):  
        """ base成员函数 """
        pass
    def delTimer( self, id ):  
        """ base成员函数 """
        pass
    def destroy( self, deleteFromDB, writeToDB ):  
        """ base成员函数 """
        pass
    def destroyCellEntity( self ):  
        """ base成员函数 """
        pass
    def teleport( self, baseEntityMB ):  
        """ base成员函数 """
        pass
    def writeToDB( self, callback, shouldAutoLoad, dbInterfaceName ):  
        """ base成员函数 """
        pass
    # 回调函数
    def onCreateCellFailure( self ):  
        """ base回调函数 """
        pass        
    def onDestroy( self ):  
       """ base回调函数 """
       pass
        
    def onGetCell( self ):  
        """ base回调函数 """
        pass        
    def onLoseCell( self ):  
        """ base回调函数 """
        pass        
    def onPreArchive( self ):  
        """ base回调函数 """
        pass        
    def onRestore( self ):  
        """ base回调函数 """
        pass        
    def onTimer( self, timerHandle, userData ):  
        """ base回调函数 """
        pass        
    def onTeleportFailure( self ):  
        """ base回调函数 """
        pass  
    def onTeleportSuccess( self, nearbyEntity ):  
        """ base回调函数 """
        pass  
    def onWriteToDB( self, cellData ):  
        """ base回调函数 """
        pass  

    class Proxy(Entity):
        # 成员函数
        def disconnect( self ):  
            """ base成员函数 """
            pass            
        def getClientType( self ):  
            """ base成员函数 """
            pass            
        def getClientDatas( self ):  
            """ base成员函数 """
            pass            
        def giveClientTo( self, proxy ):  
            """ base成员函数 """
            pass            
        def streamFileToClient( self, resourceName, desc="", id=-1 ):  
            """ base成员函数 """
            pass            
        def streamStringToClient( self, data, desc="", id=-1 ):  
            """ base成员函数 """
            pass            
        # 回调函数
        def onClientDeath( self ):  
            """ base回调函数 """
            pass
        def onClientGetCell( self ):  
            """ base回调函数 """
            pass
        def onClientEnabled( self ):  
            """ base回调函数 """
            pass
        def onGiveClientToFailure( self ):  
            """ base回调函数 """
            pass
        def onLogOnAttempt( self, ip, port, password ):
            """ base回调函数 """
            pass  
        def onStreamComplete( self, id, success ):  
            """ base回调函数 """
            pass


