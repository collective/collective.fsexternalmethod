from Products.CMFCore.DirectoryView import registerFileExtension
from App.class_init import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.CMFCore.DirectoryView import registerMetaType
from Products.CMFCore.FSObject import FSObject
from Products.ExternalMethod.ExternalMethod import ExternalMethod
from zope.interface import implements

class FSExternalMethod(FSObject, ExternalMethod):
    meta_type = 'Filesystem External Method'
    manage_options = ({'label':'Customize', 'action':'manage_main'},
                      {'label':'Test', 'action':'ZScriptHTML_tryForm',}
                     )
    
    def _createZODBClone(self):
        em = ExternalMethod(id=self.id)
        em.manage_edit(self.title, self.module, self.function, REQUEST=None)
        return em
    
    def _readFile(self, reparse):
        return

    def __init__(self, *args, **kwargs):
        super(FSExternalMethod, self).__init__(*args, **kwargs)
        props = kwargs['properties']
        self.manage_edit(props['title'], props['module'], props['function'], REQUEST=None)
        return
    
InitializeClass(FSExternalMethod)

registerFileExtension('em', FSExternalMethod)
registerMetaType('External Method', FSExternalMethod)
