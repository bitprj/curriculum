#! /bin/bash

# HOW TO USE:
#
# 1) Move exp.sh into the same directory as your cards
#
# 2) Pick a total exp amount for the entire lab
#
# 3) Determine the exp split amounts
#
# 4) Type the following command:
#
# exp.sh <exp split for 1.md> <exp split for 2.md's> <exp split for 3.md's>...as many as needed
# 
# 5) Open the file badgeDataAmounts.txt just created with the data you need
#
#
# EXAMPLE:
#
# 1) I moved exp.sh into the directory with my cards
# 
# 2) I choose the lab to be worth Python level 1 amount: 100 exp
#
# 3) There are 3 hard cards, and my exp splits are:
#      20 exp for 1.md
#      40 exp for 2.md
#      20 exp for 3.md
# 4) I then type:
#
# exp.sh 20 40 20
#
# VIEWING RESULTS
#
# A file called badgeDataAmounts.txt will get created with the info you need

bonusRate=0.1
mediumWeight=1
easyWeight=2

hardCardNum=1

outFile=badgeDataAmounts.txt

head -n1 1.md > $outFile

while [ $# -gt 0 ] ; do
    printf "Analyzing Cards for %s.md\n" $((hardCardNum))
    printf "For Hard Card: %s.md\n" $((hardCardNum)) >> $outFile

    hard=0
    medium=0
    easy=0
    for file in $hardCardNum*.md ; do
	file=${file%.md}
        chrlen=${#file}

        case $chrlen in
            1) ((hard++)) ;;
            2) ((medium++)) ;;
            3) ((easy++))
        esac
    done

    totalWeights=$(($medium * $mediumWeight + $easy * $easyWeight ))

    
    totalExp=$1

    # get bonus
    bonus=`awk -vp=$bonusRate -vq=$totalExp 'BEGIN{printf "%.2f", p * q}'`
    
    # subtract bonus
    hardExp=`awk -vp=$totalExp -vq=$bonus 'BEGIN{printf "%.2f", p - q}'`

    # get amount to subtract per medium card
    mediumExp=`awk -vp=$hardExp -vq=$totalWeights 'BEGIN{printf "%.2f", p / q}'`

    # get amount to subtract per easy card
    easyExp=`awk -vp=$mediumExp -vq=$easyWeight 'BEGIN{printf "%.2f", p * q}'`

    # truncate the exp amounts
    easyExp=${easyExp%.*}
    mediumExp=${mediumExp%.*}
    hardExp=${hardExp%.*}

    ((hardCardNum++))

    printf "bonus: %s\n" "$bonus" >> $outFile
    printf "hardExp: %s\n" "$hardExp" >> $outFile
    printf "mediumExp subtract amt: %s\n" "$mediumExp" >> $outFile
    printf "easyExp subtract amt: %s\n" "$easyExp" >> $outFile
    # FOR DEBUGGING: UNCOMMENT TO USE
#    printf "Number of hard cards: %s\n" "$hard" >> $outFile # should always be 1
#    printf "Number of medium cards: %s\n" "$medium" >> $outFile
#    printf "Number of easy cards: %s\n" "$easy" >> $outFile
#    printf "totalWeight: %s\n" "$totalWeights" >> $outFile
    printf "\n" >> $outFile
    shift
done
