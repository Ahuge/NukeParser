class Knob(object):

    def Class(self):
        """
        self.Class() -> Class name.
        @return: Class name.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def clearAnimated(self):
        """
        Clear animation for channel 'c'. Return True if successful.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def clearFlag(self, f):
        """
        self.clearFlag(f) -> None.
        Clear flag.
        @param f: Flag.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def critical(self, message):
        """
        self.critical(message) -> None.
        @param message: message to put the knob in error, and do a popup.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def debug(self, message):
        """
        self.debug(message) -> None.
        @param message: message to put out to the error console, attached to the knob, if the verbosity level is set high enough.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def enabled(self):
        """
        self.enabled() -> Boolean.
            @return: True if the knob is enabled, False if it's disabled.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def error(self, message):
        """
        self.error(message) -> None.
        @param message: message to put the knob in error.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def fromScript(self):
        """
        Initialise from script.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def fullyQualifiedName(self, channel):
        """
        self.fullyQualifiedName(channel=-1) -> string
        Returns the fully-qualified name of the knob within the node. This can be useful for expression linking.
            @param channel: Optional parameter, specifies the channel number of the sub-knob (for example, channels of  0 and 1 would refer to the x and y of a XY_Knob respectively), leave blank or set to -1 to get the  qualified name of the knob only.
        @return: The string of the qualified knob or sub-knob, which can be used directly in expression links.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def getDerivative(self):
        """
        Return derivative at time 't' for channel 'c'.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def getFlag(self, f):
        """
        self.getFlag(f) -> Bool.
        Returns whether the input flag is set.
        @param f: Flag.
        @return: True if set, False otherwise.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def getIntegral(self):
        """
        Return integral at the interval [t1, t2] for channel 'c'.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def getKeyIndex(self):
        """
        Return keyframe index at time 't' for channel 'c'.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def getKeyList(self):
        """
        Get all unique keys on the knob.  Returns list.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def getKeyTime(self):
        """
        Return index of the keyframe at time 't' for channel 'c'.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def getNthDerivative(self):
        """
        Return nth derivative at time 't' for channel 'c'.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def getNumKeys(self):
        """
        Return number of keyframes for channel 'c'.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def getValue(self):
        """
        Return value at the current frame for channel 'c'.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def getValueAt(self):
        """
        Return value at time 't' for channel 'c'.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def hasExpression(self, index):
        """
        self.hasExpression(index=-1) -> bool
        Return True if animation at index 'index' has an expression.
        @param index: Optional index parameter. Defaults to -1 if not specified. This can be specified as a keyword parameter if desired.
        @return: True if has expression, False otherwise.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def isAnimated(self):
        """
        Return True if channel 'c' is animated.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def isKey(self):
        """
        Return True if there is a keyframe at the current frame for channel 'c'.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def isKeyAt(self):
        """
        Return True if there is a keyframe at time 't' for channel 'c'.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def label(self):
        """
        self.label() -> label.
        @return: label.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def name(self):
        """
        self.name() -> name.
        @return: name.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def node(self):
        """
        self.node() -> nuke.Node
        Return the node that this knob belongs to. If the node has been cloned, we'll always return a reference to the original.
        @return: The node which owns this knob, or None if the knob has no owner yet.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def removeKey(self):
        """
        Remove key for channel 'c'. Return True if successful.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def removeKeyAt(self):
        """
        Remove key at time 't' for channel 'c'. Return True if successful.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setAnimated(self):
        """
        Set channel 'c' to be animated.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setEnabled(self, enabled):
        """
        self.setEnabled(enabled) -> None.
            Enable or disable the knob.
        @param enabled: True to enable the knob, False to disable it.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setExpression(self, expression, channel, view):
        """
        self.setExpression(expression, channel=-1, view=None) -> bool
        Set the expression for a knob. You can optionally specify a channel to set the expression for.
            @param expression: The new expression for the knob. This should be a string.
        @param channel: Optional parameter, specifying the channel to set the expression for. This should be an integer.
        @param view: Optional view parameter. Without, this command will set the expression for the current view theinterface is displaying. Can be the name of the view or the index.
        @return: True if successful, False if not.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setFlag(self, f):
        """
        self.setFlag(f) -> None.
        Logical OR of the argument and existing knob flags.
        @param f: Flag.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setLabel(self, s):
        """
        self.setLabel(s) -> None.
        @param s: New label.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setName(self, s):
        """
        self.setName(s) -> None.
        @param s: New name.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setTooltip(self, s):
        """
        self.setTooltip(s) -> None.
        @param s: New tooltip.
        @return: None.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setValue(self):
        """
        self.setValue(val, chan) -> bool
            Sets the value 'val' at channel 'chan'.
        @return: True if successful, False if not.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setValueAt(self):
        """
        self.setValueAt(val, time, chan) -> bool
            Sets the value 'val' at channel 'chan' for time 'time'.
        @return: True if successful, False if not.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def setVisible(self, visible):
        """
        self.setVisible(visible) -> None.
            Show or hide the knob.
        @param visible: True to show the knob, False to hide it.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def toScript(self):
        """
        toScript(quote, context=current) -> string.
            Return the value of the knob in script syntax.
        Pass True for quote to return results quoted in {}.
        Pass None for context to get results for all views and key times (as stored in a .nk file).
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def tooltip(self):
        """
        self.tooltip() -> tooltip.
        @return: tooltip.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def value(self):
        """
        Return value at the current frame for channel 'c'.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")

    def visible(self):
        """
        self.visible() -> Boolean.
            @return: True if the knob is visible, False if it's hidden.
        """
        raise NotImplementedError("This function is not written yet. Please put in an issue on the github page.")
