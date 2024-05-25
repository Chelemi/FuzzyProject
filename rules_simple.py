RULES = []

# Days Worn Variable
RULES.append("IF "
             "(Days_worn IS one) OR "
             "(Days_worn IS two) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS three) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS four)  "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS five)  "
             "THEN "
             "(Output IS dirty)")


# Days left out Variable
RULES.append("IF "
             "(Days_left_out IS one) OR "
             "(Days_left_out IS two)  "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_left_out IS three)  "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_left_out IS four) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_left_out IS five) "
             "THEN "
             "(Output IS dirty)")

# Activity Variable
RULES.append("IF "
             "(Activity IS none) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Activity IS some) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Activity IS medium) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Activity IS a_lot) OR "
             "(Activity IS full) "
             "THEN "
             "(Output IS dirty)")

# Stress Variable
RULES.append("IF "
             "(Stress IS none) OR "
             "(Stress IS some) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Stress IS medium) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Stress IS a_lot) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Stress IS full) "
             "THEN "
             "(Output IS dirty)")

# Temperature Variable
RULES.append("IF "
             "(Temperature IS cold) OR "
             "(Temperature IS fresh) OR "
             "(Temperature IS temperate) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Temperature IS warm) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Temperature IS hot) "
             "THEN "
             "(Output IS somewhat_dirty)")

# Hours worn Variable
RULES.append("IF "
             "(Hours IS two) OR "
             "(Hours IS four) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Hours IS six) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Days left out Variable
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS one) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS two) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS three) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS four) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Days_left_out IS five) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS one) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS two) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS three) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS four) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Days_left_out IS five) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS one) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS two) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS three) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS four) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Days_left_out IS five) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Activity Variable
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Activity IS none) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Activity IS some) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Activity IS medium) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Activity IS a_lot) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Activity IS full) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Activity IS none) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Activity IS some) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Activity IS medium) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Activity IS a_lot) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Activity IS full) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Activity IS none) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Activity IS some) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Activity IS medium) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Activity IS a_lot) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Activity IS full) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Stress Variable
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Stress IS none) "
             "THEN "
             "(Output IS clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Stress IS some) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Stress IS medium) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Stress IS a_lot) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS one) AND "
             "(Stress IS full) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Stress IS none) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Stress IS some) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Stress IS medium) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Stress IS a_lot) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Stress IS full) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Stress IS none) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Stress IS some) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Stress IS medium) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Stress IS a_lot) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Stress IS full) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Temperature Variable
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Temperature IS cold) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Temperature IS fresh) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Temperature IS temperate) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Temperature IS warm) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Temperature IS hot) "
             "THEN "
             "(Output IS dirty) ")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Temperature IS cold) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Temperature IS fresh) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Temperature IS temperate) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Temperature IS warm) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Temperature IS hot) "
             "THEN "
             "(Output IS dirty)")

# Days worn and Hours Variable
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat_clean)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Hours IS four) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Hours IS six) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS two) AND "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Hours IS four) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Hours IS six) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Days_worn IS three) AND "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")

# Activity Variable and hours
RULES.append("IF "
             "(Activity IS some) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS somewhat_dirty)")
RULES.append("IF "
             "(Activity IS some) AND "
             "(Hours IS four) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS some) AND "
             "(Hours IS six) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS some) AND "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS some) AND "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")

RULES.append("IF "
             "(Activity IS medium) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS medium) AND "
             "(Hours IS four) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS medium) AND "
             "(Hours IS six) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS medium) AND "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS medium) AND "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")

RULES.append("IF "
             "(Activity IS a_lot) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS a_lot) AND "
             "(Hours IS four) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS a_lot) AND "
             "(Hours IS six) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS a_lot) AND "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS a_lot) AND "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")

RULES.append("IF "
             "(Activity IS full) AND "
             "(Hours IS two) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS full) AND "
             "(Hours IS four) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS full) AND "
             "(Hours IS six) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS full) AND "
             "(Hours IS twelve) "
             "THEN "
             "(Output IS dirty)")
RULES.append("IF "
             "(Activity IS full) AND "
             "(Hours IS more) "
             "THEN "
             "(Output IS dirty)")


