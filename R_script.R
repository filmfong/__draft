mann_test <- function(x,y) {
  return (wilcox.test(x,y, alternative = "two.sided", paired = FALSE, exact = TRUE, correct = TRUE))
}

wilcox_test <- function(x,y) {
  return(wilcox.test(x,y, alternative = "two.sided", paired = TRUE, exact = TRUE, correct = TRUE))
}
