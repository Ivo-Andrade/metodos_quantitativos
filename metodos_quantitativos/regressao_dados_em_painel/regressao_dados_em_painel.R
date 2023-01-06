# library("plm")

# # plm - Panel Linear Model
# data("Grunfeld", package = "plm")
# p <- plm(inv ~ value + capital,
#          data = Grunfeld, model = "pooling")

# wi <- plm(inv ~ value + capital,
#           data = Grunfeld, model = "within", effect = "twoways")

# swar <- plm(inv ~ value + capital,
#             data = Grunfeld, model = "random", effect = "twoways")

# amemiya <- plm(inv ~ value + capital,
#                data = Grunfeld, model = "random", random.method = "amemiya",
#                effect = "twoways")

# walhus <- plm(inv ~ value + capital,
#               data = Grunfeld, model = "random", random.method = "walhus",
#               effect = "twoways")
# summary(p)
# install.packages("httpgd",repos = "http://cran.us.r-project.org")

# remotes::install_github("ManuelHentschel/vscDebugger")