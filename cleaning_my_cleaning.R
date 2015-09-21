setwd("~/Documents/Toastmasters/datawork/")

## the first csv which was a horrible mess!
# gods <- read.csv("TMY2014attend.csv", header = FALSE, col.names = c("date", paste("x", 1:6)))

# colnames(gods) <- paste("x", 1:ncol(gods), sep = "")


# house_cleaning <- function(var1){
# 	mdate <- lapply(gods[,var1], function(x) x <- strsplit(x, ",")[[1]][1])
# 	clean_dates <- unlist(lapply(mdate, function(x) x <- gsub("(\\\"|\\[|\\]|\\')", "", x)))
# 	mrole <- lapply(gods[,var1], function(x) x <- strsplit(x, ",")[[1]][2])
# 	clean_role <- unlist(lapply(mrole, function(x) x <- tolower(gsub("\\'| ", "", x))))
# 	mmember <- lapply(gods[,var1], function(x) x <- strsplit(x, ",")[[1]][3])
# 	clean_members <- unlist(lapply(mmember, function(x) x <- gsub("\\'|\\\\n|\\]", "", x)))
# 	tmpdf <- data.frame(meeting_date = clean_dates, role = clean_role, member = clean_members)
# 	return(tmpdf)
# }

# master_list <- lapply(colnames(gods), function(x) house_cleaning(x))

## take 2 with a better looking csv
gods <- read.csv("TMY2014attend.csv", header = FALSE, col.names = c("date", paste("x", 1:6)))
gods$date <- unlist(lapply(gods$date, function(x) x <- gsub("\\'|\\[|\\]", "", x)))
ghelp <- subset(gods, x.1 != "")

test <- as.character(ghelp[47,])

almost_there <- apply(ghelp, 1, function(x){
	dt <- x[1]	
	role <- as.character()
	names <- as.character()
	for(i in 2:length(x)){
		role <- c(role, strsplit(x, ",")[[i]][1])
		names <- c(names, strsplit(x, ",")[[i]][2])
	}
	return(data.frame(meeting_date = rep(dt, length(role)), role = role, member = names))
})

masterdf <- do.call(rbind, almost_there)
masterdf$role <- tolower(masterdf$role)
## trim leading whitespace 
masterdf$role <- gsub("^\\s+", "", masterdf$role)

## clean the trailing line break after the names
masterdf$member <- gsub("\\\n|^\\s+", "", masterdf$member)
master_meeting_roles <- subset(masterdf, !is.na(role) & !(role %in% c("best speaker", "best evaluator", "model speaker", 
																		"special guest speaker", "best table topics")) &
														!(member %in% c("TBD", "Tie between Nadine and Marla")))


## match master list names with roster names:
roster <- read.csv("../Roster/MembershipRoster2015Sept.csv")

## pull the first name from the offcial member list
match_pat <- roster$Name
names(match_pat) <- unlist(lapply(roster$Name, function(x) x <- strsplit(x, " ")[[1]][1]))

master_meeting_roles$first_name <- unlist(lapply(master_meeting_roles$member, function(x) x <- strsplit(x, " ")[[1]][1]))
master_meeting_roles$official_names <- match_pat[master_meeting_roles$first_name]


### names that need to be added to the database:
non_mem <- subset(master_meeting_roles, is.na(official_names))


#### export names to csv to try running entity resolution on them in python:
# write.csv(unique(master_meeting_roles$member), "minutes_members.csv", row.names = FALSE)
# write.csv(match_pat, "roster_members.csv", row.names = FALSE)

### create a map from 'resolved' list:
matches <- read.csv("./matches.csv", header = FALSE)
mem_map <- unlist(lapply(matches$V1, function(x) x <- gsub("(\\'|\\[|\\])", "", x))) 
names(mem_map) <- matches$V2

master_meeting_roles$official_names <- mem_map[tolower(master_meeting_roles$member)]


### to finish the cleaning manually, source("manual_cleaning.R"). This is saved to a different file to protect the identities of our members.
