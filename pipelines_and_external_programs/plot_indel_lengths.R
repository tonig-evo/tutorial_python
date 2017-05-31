library(ggplot2)

args <- commandArgs(TRUE)
csv_in = args[1]
png_out = args[2]

length_data <- read.csv(csv_in, header=FALSE)

len_plot = ggplot(length_data, aes(x=V1, y=V2))+
            geom_bar(stat='identity', position='dodge', fill='steel blue') +
            xlab('Indel Length (bp)') + ylab('Number of INDELs') +
            xlim(0, 20) +
            theme_bw()

ggsave(png_out, len_plot, height=6, width=9)