#------------------------------------------#
# Title: ProcessingClasses.py
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Deborah C, 2022-Dec-11, Modified functionality
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself.')

import DataClasses as DC

class DataProcessor:
    """Processes the data in the application
    
    properties:
        
        
        
    methods:        
      add_CD(CDInfo, table): -> None.
      select_cd(table: list, cd_idx: int) -> DC.CD.
      add_track(track_info: tuple, cd: DC.CD) -> None.
      remove_track(track_id: int, cd: DC.CD) -> None.
    
    """
    @staticmethod
    def add_CD(CDInfo, table):
        """Function that adds CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer.')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """Function that selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return.

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        # TODONE add code as required
        try:
            cd_idx = int(cd_idx)
        except ValueError as e:
            print('ID is not an integer.')
            print(e.__doc__)
        for cd in table:
            if cd.cd_id == cd_idx:
                return cd
        raise Exception('This CD / Album index does not exist.')
       
    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """Function that adds a Track object with attributes in track_info to CD.


        Args:
            track_info (tuple): Tuple containing track info (position, title, length).
            cd (DC.CD): cd object the track gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None.

        """

        # TODONE add code as required
        trackID, title, length = track_info
        try:
            trackID = int(trackID)
        except:
            raise Exception('ID must be an integer.')
        track = DC.Track(trackID, title, length)
        cd.add_track(track)
        
    @staticmethod
    def remove_track(track_id: int, cd: DC.CD) -> None:
        """Function that removes a Track object from a CD object's track list

        Args:
            track_id (int): Integer ID of a Track object within the CD object's track list.
            cd (DC.CD): cd object the track gets added to.


        Raises: 
            Exception: DESC raised in case track_id is not an integer.

        Returns:
            None.

        """               
        try:
            track_id = int(track_id)
        except:
            raise Exception('ID must be an integer.')
            










