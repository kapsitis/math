require(grid)
require(lattice)
require(gridSVG)
require(pxR)
require(sp)
require(latticeExtra)
require(maptools)
require(classInt)
require(colorspace)
require(RCurl)
require(gdata)
require(Unicode)

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

#source("schoolUtilities.R")

#cspVecumi <- read.table (file = "IS0060.A.csv", header = TRUE, sep = ",", encoding = "UTF-8")
#cspNovadi <- read.table (file = "IS0181.A.csv", header = TRUE, sep = ",", encoding = "UTF-8")
#amoFactor <- sum(cspVecumi$Pavisam2016[13:20])/sum(cspVecumi$Pavisam2016[8:19])
#cspNovadi <- mutate(cspNovadi, AmoSkoleni = round(amoFactor*Skoleni2016))
#cspNovadi$Teritorija <-  toupper(sapply(as.vector(cspNovadi$Teritorija),strFromUnicode))

#resultDf <- getAllResults()
# resultDf$UpperMunicipality <- 
#   toupper(sapply(as.vector(resultDf$Municipality),strFromUnicode))
#novadiTable <- table(resultDf$Municipality)
#novadiDf <- data.frame(Novadi = as.character(as.vector(names(novadiTable))), Dalibnieki = as.vector(novadiTable))
#novadiDf$Teritorija <- toupper(sapply(as.vector(novadiDf$Novadi),strFromUnicode))

#mergedNovadi <- merge(novadiDf, cspNovadi, by.x = "Teritorija", by.y="Teritorija", all.x = TRUE)
#mergedNovadi <- mutate(mergedNovadi, Intensity = Dalibnieki/AmoSkoleni)
#novadiByGender <- count(resultDf, vars=c("Dzimums","Municipality"))
#novadiFemale <- novadiByGender[novadiByGender$Dzimums == "Female",]
#novadiFemale <- rename(novadiFemale, c("freq"="FF"))
#novadiFemale <- subset(novadiFemale, select = c("Municipality", "FF"))
#novadiMale <- novadiByGender[novadiByGender$Dzimums == "Male",]
#novadiMale <- rename(novadiMale, c("freq"="MM"))
#novadiMale <- subset(novadiMale, select = c("Municipality", "MM"))

#mergedNovadi <- merge(mergedNovadi, novadiFemale, by.x = "Novadi", by.y = "Municipality", all.x = TRUE)
#mergedNovadi <- merge(mergedNovadi, novadiMale, by.x = "Novadi", by.y = "Municipality", all.x = TRUE)

#mergedNovadi$FF[is.na(mergedNovadi$FF)] <- 0
#mergedNovadi$MM[is.na(mergedNovadi$MM)] <- 0



# intensityFrame <- 
#   data.frame(loc = allChMun$Location, # Teritorija
#              per = olympParticipation, # Intensity
#              cc = olympCC,  # amoSkoleni
#              pp = olympPP, # dalibnieki
#              mm = olympMM,  # zeni
#              ff = olympFF)  #meitenes


## novadu data.frame
novFrame <- read.table(
  file="maps/lv-municipalities.csv", 
  sep=",",
  header=TRUE,
  row.names=NULL,  
  fileEncoding="UTF-8")

## Standardize every municipality ID to 7 digits
novFrame$Classifier <- 
  sapply(novFrame$Classifier, function(arg) { sprintf("%07.0f",arg) })


mapSHP <-  readShapePoly(fn = "maps/Export_Output")
mapaDat <- as.data.frame(mapSHP)
mapaIDs <- as.numeric(rownames(mapaDat))

panel.str <- deparse(panel.polygonsplot, width=500)
panel.str <- sub("grid.polygon\\((.*)\\)",
  "grid.polygon(\\1, name=paste('ID', slot(pls\\[\\[i\\]\\], 'ID'\\), sep=':'))",
  panel.str)
panel.polygonNames <- eval(parse(text=panel.str),
                           envir=environment(panel.polygonsplot))



#bigdata <- merge(mapaDat, novFrame, sort=FALSE, 
#                 by.x="ATVK", by.y="Classifier")
#biggerdata <- merge(bigdata,mergedNovadi, sort=FALSE, 
#                    by.x="UpperName", by.y="Teritorija")
						   
#n=7
# workaround - stretch the interval a little bit
#theVector = c(min(biggerdata$Intensity)*0.999,
#              as.vector(biggerdata$Intensity),max(biggerdata$Intensity)*1.001)
#int <- classIntervals(theVector, n, style='jenks')
#pal <- brewer.pal(n, 'Reds')
palWhite <- c("#ffffff", pal)
#brksWhite <- c(0, 0.000001,int$brks[-1])

# Possible palettes: Blues BuGn BuPu GnBu Greens Greys Oranges 
# OrRd PuBu PuBuGn PuRd Purples RdPu Reds YlGn 
# YlGnBu YlOrBr YlOrRd

#Total <- biggerdata$Intensity
#mapSHP@data <- cbind(mapSHP@data, novFrame)
#p <- spplot(mapSHP["Total"]) #, panel=panel.polygonNames)#,
#            #col.regions=palWhite, at=brksWhite)
#p

## grobs in the graphical output
grobs <- grid.ls()
## only interested in those with "GRID." in the name
nms <- grobs$name[grobs$type == "grobListing"]
idxNames <- grep("GRID", nms)
IDs <- nms[idxNames]


theCount <- 1
for (id in unique(IDs)){
  dat <- biggerdata[which(bigdata$Grob==id),]
#  info <-  paste0(dat$FullName, ": ", round(100*dat$Intensity,2), "%")  
  g <- grid.get(id)
  
#  theMM <- mergedNovadi$MM[mergedNovadi$Teritorija == dat$UpperName]
#  theFF <- mergedNovadi$FF[mergedNovadi$Teritorija == dat$UpperName]
#  theCC <- mergedNovadi$AmoSkoleni[mergedNovadi$Teritorija == dat$UpperName]
#  info2 <- sprintf("%1.0fM,%1.0fF no %1.0f",theMM, theFF, theCC)
  ## attach SVG attributes
#  grid.garnish(id,
#               onmouseover=paste("showTooltip(evt, '", info, "','",info2,"')"),
#               onmouseout="hideTooltip()")
  theCount <- theCount + 1 
}

#grid.script(filename="maps/tooltip.js")

grid.export("novadi.svg")
