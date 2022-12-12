#------------------------------------------#
# Title: IOClasses.py
# Desc: A Module for IO Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Deborah C, 2022-Dec-11, Modified functionality
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself.')

import DataClasses as DC
import ProcessingClasses as PC

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name: list, lst_Inventory: list) -> None:
        """Function that saves 

        Args:
            file_name (list): list of file names [CD Inventory, Track Inventory] that hold the data.
            lst_Inventory (list): list of CD objects.

        Returns:
            None.

        """

        # TODONE modify method to accept a list of file names.
        file_name_CD = file_name[0]
        file_name_track = file_name[1]
        try:
            with open(file_name_CD, 'w') as file:
                for disc in lst_Inventory:
                    file.write(disc.get_record())
            # TODONE add code to save track data to file
            with open(file_name_track, 'w') as file:
                for disc in lst_Inventory:
                    tracks = disc.cd_tracks
                    disc_id = disc.cd_id
                    for track in tracks:
                        if track is not None:
                            record = '{},{}'.format(disc_id, track.get_record())
                            file.write(record)
        except Exception as e:
            print('There was a general error.', e, e.__doc__, type(e), sep='\n')

    @staticmethod
    def load_inventory(file_name: list) -> list:
        """Function that loads CD data from a set of files.

        Args:
            file_name (list): List of file names [CD Inventory, Track Inventory] that hold the data.

        Returns:
            list: List of CD objects.

        """
        lst_Inventory = []
        # TODONE modify method to accept a list of file names
        file_name_CD = file_name[0]
        file_name_track = file_name[1]
        try:
            with open(file_name_CD, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    row = DC.CD(data[0], data[1], data[2])
                    lst_Inventory.append(row)
            # TODONE add code to load track data
            with open(file_name_track, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    cd = PC.DataProcessor.select_cd(lst_Inventory, int(data[0]))
                    track = DC.Track(int(data[1]), data[2], data[3])
                    cd.add_track(track)
                return lst_Inventory
        except Exception as e:
            print('There was a general error.', e, e.__doc__, type(e), sep='\n')
        return lst_Inventory
 
class ScreenIO:
    """Handling Input / Output
    
    properties:

    functions:
        print_menu(): -> None
        menu_choice() -> The user's choice from the menu

    """

    @staticmethod
    def print_menu():
        """Function that displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print()
        print('Main Menu\n\n[l] Load Inventory from File\n[a] Add CD / Album\n[d] Display Current Inventory')
        print('[c] Choose CD / Album\n[s] Save Inventory to File\n[x] eXit\n')

    @staticmethod
    def menu_choice():
        """Function that gets user input for menu selection

        Args:
            None.

        Returns:
            Choice (string): A lower case string of the user's input choices: l, a, d, c, s, or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 'c', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, d, c, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def print_CD_menu():
        """Function that displays a sub menu of choices for CD / Album to the user

        Args:
            None.

        Returns:
            None.
        """
        print()
        print('CD Sub Menu\n\n[a] Add track\n[d] Display cd / Album details\n[r] Remove track\n[x] eXit to Main Menu')

    @staticmethod
    def menu_CD_choice():
        """Function that gets user input for CD sub menu selection

        Args:
            None.

        Returns:
            choice (string): A lower case string of the user's input choices: a, d, r, or x

        """
        choice = ' '
        while choice not in ['a', 'd', 'r', 'x']:
            print()
            choice = input('Which operation would you like to perform? [a, d, r, or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Function that displays current inventory table


        Args:
            Table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')

    @staticmethod
    def show_tracks(cd):
        """Displays the Tracks on a CD / Album

        Args:
            cd (CD): CD object.

        Returns:
            None.

        """
        if len(cd.cd_tracks) == 0:
            return
        print()
        print('====== Current CD / Album: ======')
        print(cd)
        print('=================================')
        print(cd.get_tracks())
        print('=================================')

    @staticmethod
    def get_CD_info():
        """Function that requests CD information from User to add CD to inventory


        Returns:
            cdId (string): Holds the ID of the CD dataset.
            cdTitle (string): Holds the title of the CD.
            cdArtist (string): Holds the artist of the CD.

        """

        cdId = input('Enter ID Number: ').strip()
        cdTitle = input('What is the CD\'s Title? ').strip()
        cdArtist = input('What is the Artist\'s name? ').strip()
        return cdId, cdTitle, cdArtist

    @staticmethod
    def get_track_info():
        """Function that requests Track information from User to add Track to CD / Album


        Returns:
            trkId (string): Holds the ID of the Track within the Track dataset.
            trkTitle (string): Holds the title of the Track.
            trkLength (string): Holds the length (time) of the Track.

        """

        trkId = input('Enter position on CD / Album: ').strip()
        trkTitle = input('What is the Track\'s title? ').strip()
        trkLength = input('What is the Track\'s length? ').strip()
        return trkId, trkTitle, trkLength
    
    @staticmethod
    def get_track_id():
        """Function that requests Track ID for Track removal
        
        
        Returns:
            trkId (string): Holds the ID of the Track to remove
            
        """
        print()
        trkId = input('Enter the ID of the track you wish to remove: ').strip()
        return trkId
