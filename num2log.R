#######################################
# CONVERT NUMERIC FEATURES TO LOGICAL #
#######################################

num2log = function(data) {
    
    # Count the number of rows
    n.row = nrow(data)
    
    # Count the number of unique values in numeric features
    n.unq = countUnique(data[, vapply(data, is.numeric, T)])
    
    # Identify features that should be logical
    log.ind = sapply(data[, names(n.unq)[n.unq <= 3]], unique)
    log.ind = vapply(log.ind, function(z) all(z %in% c(0, 1, NA)), T)
    
    # Convert numeric features to logical
    log.names = names(log.ind)[which(log.ind)]
    data[, log.names] = vapply(data[, log.names], as.logical, logical(n.row))
    
    # Report results
    print(paste('Created', sum(log.ind), 'logical features.'), quote = F)
    
    # Return data
    return(data)
    
}
