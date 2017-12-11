##########################################################################
##                                                                      ##
##                      SYSTEM CONTROL SOFTWARE PAGE                    ##
##                                                                      ##
##########################################################################

# Modules Required by BamInsight System module
import main
import UCSCFiles

#######################################################################
#            GLOBAL VARIABLES DEFINED DURING EXECUTION                #
#######################################################################

finalBW_F = ""
finalBW_R = ""




def system():
    # accept the inputs and check their reliability
    args = main.argsNcheckers()

    # create files of chromossome sizes
    main.createChrLengthFiles(args.genome)



    for enum,BamFile in enumerate(args.name):
        #Preparing Final files
        UCSCFiles.createMainDirectory(args.long_label[enum], args.create_dir)
        UCSCFiles.writeGenomesFile(args.genome, args.create_dir)
        UCSCFiles.writeHub(args.long_label[enum], args.short_label[enum], args.email, args.create_dir)
        UCSCFiles.createGenomeDirectory(args.genome, args.create_dir)


        # Handling BAM file
        NamesFilesPerStrand, ReadsPerStrand =main.splitBamFilePerStrands(BamFile, args.basename[enum], args.flags_forward, args.not_flags_forward,
                                        args.flags_reverse, args.not_flags_reverse)
        #Create BedGraphs
        BedGraphsCreated = main.createBedGraph(NamesFilesPerStrand, ReadsPerStrand)

        #Create BigWigs
        BWnames = main.createBWFromBedGraph(BedGraphsCreated)
        finalBW_F, finalBW_R = BWnames[0] , BWnames[1]

        #Write TrackDB of Final Files
        UCSCFiles.writeTrackDB(args.long_label[enum], args.short_label[enum], finalBW_F, finalBW_R, args.create_dir)

system()
