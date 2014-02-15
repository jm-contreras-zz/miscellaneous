# Clear workspace of current environment
clearws = function(e = .GlobalEnv) {    
    remove(list = ls(e)[sapply(ls(e), function(n){!is.function(get(n))})],
           envir = e)
}

# Compute standard error of the mean
se = function (x) {   
    return(sqrt(var(x) / length(x)))
}

# Count how much time elapses
clock = function(which.time, start) {
    if (which.time == 'tic') {
        time = Sys.time()
    } else if (which.time == 'toc') {
        time = Sys.time() - start
    } else {
        warning('Tic or toc. Something else I cannot.')
    }
    return(time)
}

# Compute the mode
stat.mode = function(x) {
    ux = unique(x)
    ux[which.max(tabulate(match(x, ux)))]
}

# Source a batch of files
sourceBatch = function(dir, func.list) {
    n.func = length(func.list)
    for (i.func in 1:n.func) {
        this.func = paste(func.list[i.func], '.R', sep = '')
        source(file.path(dir, this.func))
    }
}

# Count the number of unique values in each variable of a matrix or data frame
countUnique = function(data) {
    data = vapply(sapply(data, unique), length, 0)
    return(data)
}
