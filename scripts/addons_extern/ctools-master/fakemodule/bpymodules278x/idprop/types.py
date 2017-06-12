class IDPropertyArray:
    """"""

    def to_list(self):
        """Return the array as a list."""

    typecode = None
    """The type of the data in the array {'f': float, 'd': double, 'i': int}."""


class IDPropertyGroup:
    """"""

    def clear(self):
        """Clear all members from this group."""

    def get(self, key, default=None):
        """Return the value for key, if it exists, else default."""

    def items(self):
        """Return the items associated with this group."""

    def iteritems(self):
        """Iterate through the items in the dict; behaves like dictionary method iteritems."""

    def keys(self):
        """Return the keys associated with this group as a list of strings."""

    def pop(self, key):
        """Remove an item from the group, returning a Python representation.
        
        :param key: Name of item to remove.
        :type key: str
        """

    def to_dict(self):
        """Return a purely python version of the group."""

    def update(self, other):
        """Update key, values.
        
        :param other: Updates the values in the group with this.
            (type: idprop.types.IDPropertyGroup or dict)
        :type other: IDPropertyGroup or dict
        """

    def values(self):
        """Return the values associated with this group."""

    name = None
    """The name of this Group."""


class IDPropertyGroupIter:
    """"""
