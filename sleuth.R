#kallisto_samples.txt

#load sleuth package 
library(sleuth)
#load the dplyr package for data frame filtering 
library(dplyr)

library(data.table)

#directory<-getwd()

#directory<-paste(directory, "/miniProject_Aditi_Patel", sep= "")

#sample_ids<-dir(file.path(directory))
#sample_ids<-c('SRR5660030', 'SRR5660033', 'SRR5660044', 'SRR5660045') 

#conditions<-c("2dpi", "6dpi", "2dpi", "6dpi") 
#str(conditions)

#paths<-file.path(directory,sample_ids)
#paths<-c('miniProject_Aditi_Patel/SRR5660030', 'miniProject_Aditi_Patel/SRR5660033', 'miniProject_Aditi_Patel/SRR5660044', 'miniProject_Aditi_Patel/SRR5660045')

#stab<-as.data.frame(cbind(sample_ids, conditions, paths)) 

#colnames(stab)<-c("sample", "condition", "path") 

#stab$sample<-as.character(stab$sample) 
#stab$condition<-as.character(stab$condition)
#stab$path<-as.character(stab$path)
#stab

stab<-read.table("kallisto_table.txt",header=TRUE,stringsAsFactors=FALSE,sep='\t')

#initialize sleuth object
so<-sleuth_prep(stab)


#fit a model comparing two conditions 

so<-sleuth_fit(so,~condition,'full')

#fit the reduced model to compare in the likelihood ratio test
so<-sleuth_fit(so,~1,'reduced')

#perform the likelihood ratio test for differential expression between conditions (2dpi & 6dpi)
so<-sleuth_lrt(so,'reduced','full')

#extract the test results from the sleuth object 
sleuth_table<-sleuth_results (so,'reduced:full','lrt',show_all=FALSE)

#filter most significant results (FDR/qval <0.05) and sort by pval 
sleuth_significant<-dplyr::filter(sleuth_table,qval<=0.05)%>%dplyr::arrange(pval)
sleuth_output<-sleuth_significant %>% select(target_id,test_stat,pval,qval)

#write FDR <0.05 transcripts to file 
write.table(sleuth_output,file='miniProject_Aditi_Patel/sleuth_output.txt', quote=FALSE,row.names=FALSE)