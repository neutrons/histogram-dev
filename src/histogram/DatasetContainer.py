#!/usr/bin/env python
# Timothy M. Kelley Copyright (c) 2005 All rights reserved
import logging

logger = logging.getLogger("Histogram")


class DatasetContainer(object):
    """Container of dataset objects"""

    def addDataset(self, name, id, dataset):
        """addDataset( name, id, dataset) -> None
        Add the dataset to this container.
        Inputs:
            name: name of this dataset (string)
            id: id of this dataset (integer)
        Output:
            None
        Exceptions: ValueError
        Notes: name and id must be unique within this container"""
        # 1. store by name
        if name not in self._byNames:
            self._byNames[name] = dataset
            logger.debug("{0!s} added dataset {1!s}".format(self, name))
        else:
            msg = "container already has dataset named {0!s}".format(name)
            raise ValueError(msg)

        # 2. store by id
        if id not in self._byIds:
            self._byIds[id] = [name, dataset]
        else:
            msg = "container already has dataset with id {0!s}".format(id)
            raise ValueError(msg)

        self._id2name[id] = name
        self._name2id[name] = id
        return

    def deleteDataset(self, name=None, id=None):
        if name and name not in self._byNames:
            raise ValueError("dataset {0!s} not found in container".format(name))
        if id and id not in self._byIds:
            raise ValueError("dataset {0!s} not found in container".format(id))

        if name is None and id is None:
            return  # nothing to delete

        name = name or self._id2name[id]
        id = id or self._name2id[name]

        del self._byNames[name]
        del self._byIds[id]
        del self._id2name[id]
        del self._name2id[name]
        return

    def replaceDataset(self, name=None, dataset=None, id=None):
        """replaceDataset( name, dataset) -> None
        replace the dataset in this container.
        Inputs:
            name: name of this dataset (string)
        Output:
            None
        Exceptions: ValueError
        """
        if dataset is None:
            raise ValueError("dataset is not specified")

        if name is None and id is None:
            return

        if name and name not in self._byNames:
            raise ValueError("dataset {0!s} not found in container".format(name))
        if id and id not in self._byIds:
            raise ValueError("dataset {0!s} not found in container".format(id))

        name = name or self._id2name[id]
        id = id or self._name2id[name]

        logger.debug("{0!s} replaced dataset {1!s} (id={2!s})".format(self, name, id))

        self._byNames[name] = dataset
        self._byIds[id] = [name, dataset]
        return

    def datasetFromName(self, name):
        """datasetFromName( name) -> dataset"""
        ds = None
        try:
            ds = self._byNames[name]
        except KeyError:
            msg = "No dataset named {0!s}. Available datasets: {1!s}".format(
                name, list(self._byNames.keys())
            )
            raise KeyError(msg)
        return ds

    def datasetFromId(self, id):
        """datasetFromId( id) ->"""
        ds = None
        try:
            ds = self._byIds[id][1]
        except KeyError:
            msg = "No dataset with id {0!s}".format(id)
            raise KeyError(msg)
        return ds

    def listDatasets(self):
        """listDatasets() -> [(id, name)]
        Input:
            None
        Output:
            List of tuples of id & name for each dataset
        Exceptions: None
        Notes: None"""
        datasets = [(item[0], item[1][0]) for item in list(self._byIds.items())]
        return datasets

    def __init__(self):
        """DatasetContainer() -> new dataset container"""
        self._byNames = {}  # stores name:dataset
        self._byIds = {}  # stores id:[name, dataset]
        self._id2name = {}
        self._name2id = {}
        return


# version
__id__ = "$Id$"

# End of file
