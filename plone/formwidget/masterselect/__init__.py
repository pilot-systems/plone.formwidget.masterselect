from plone.formwidget.masterselect.interfaces import (IMasterSelectBoolField,
                                                      IMasterSelectField,
                                                      IMasterSelectRadioField)
from plone.formwidget.masterselect.widget import (MasterSelectBoolFieldWidget,
                                                  MasterSelectFieldWidget,
                                                  MasterSelectRadioFieldWidget,
                                                  MasterSelectWidget)
from zope.i18nmessageid import MessageFactory
from zope.interface import implementer
from zope.schema import Bool, Choice

_ = MessageFactory("plone.formwidget.masterselect")


@implementer(IMasterSelectField)
class MasterSelectField(Choice):
    """MasterSelectField that provides additional properties for widget
    (extends schema.Choice)
    """

    slave_fields = ()

    def __init__(self,
        slave_fields=(),
        **kw
    ):
        self.slave_fields = slave_fields
        super(MasterSelectField, self).__init__(**kw)


@implementer(IMasterSelectBoolField)
class MasterSelectBoolField(Bool):
    """MasterSelectBoolField that provides addtional properties for widget
    (extends schema.Bool)
    """

    slave_fields = ()

    def __init__(self,
        slave_fields=(),
        **kw
    ):
        self.slave_fields = slave_fields
        super(MasterSelectBoolField, self).__init__(**kw)


@implementer(IMasterSelectRadioField)
class MasterSelectRadioField(Choice):
    """MasterSelectRadioField that provides additional properties for widget
    (extends schema.Choice)
    """

    slave_fields = ()

    def __init__(self,
        slave_fields=(),
        **kw
    ):
        self.slave_fields = slave_fields
        super(MasterSelectRadioField, self).__init__(**kw)
