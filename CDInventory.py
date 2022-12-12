#------------------------------------------#
# Title: CDInventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Deborah C, 2022-Dec-11, Modified functionality
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('\nType \'yes\' to continue and reload from file. Otherwise, reload will be canceled. ')
        if strYesNo.lower() == 'yes':
            print('Reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)            
        else:
            input('Canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu. ')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = input('Select the CD / Album Index Number: ')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        # TODONE add code to handle tracks on an individual CD
        while True: 
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()
            if strChoice == 'x':
                break
            if strChoice == 'a':
                IO.ScreenIO.show_tracks(cd)
                tplTrackInfo = IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(tplTrackInfo, cd)
                IO.ScreenIO.show_tracks(cd)
                continue
            elif strChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
                continue
            elif strChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                trk_id = IO.ScreenIO.get_track_id()
                PC.DataProcessor.remove_track(trk_id, cd)
                print()
                print('Track removed.')
                print()
                IO.ScreenIO.show_tracks(cd)
            else:
                print('General Error')      
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n]: ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu. ')
        continue  # start loop back at top.
    else:
        print('General Error')