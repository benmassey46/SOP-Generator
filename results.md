
## Results

Rank order each model from each provider fot text generation
e.g. 
gpt-4o
gpt-4-turbo
gpt
do the same for gemini and claude. 
probably need some links to support this ranking

select 2 or 3 SOP types

for each SOP type

generate SOP using a pair of models* 

* auto calculate review metrics for each model pair

* auto calculate difference metrics for each model pair

* auto calculate structure and content differences 

*pair of models - compare the top most ranked 
and then between the top most ranked and worst ranked
the idea being to show the best SOP generation possible 
and any gap between best and worst for the 
SOP generation task 

*could also do multiple runs with the same model pairs 
and see if the metrics significantly difference

discuss the metrics, do they align when comparing the best models, are they significantly different comparing 
best to worse ranked model?

I would also do 
some manual checking to see if anything doesn't make sense
i.e. the model wandered off topic or made syntax/format errors in the output

-----------------------------------
feed the expert file into the few shot examples and generate SOP for the best (and maybe worse models)  

calculate diff, review and structure metrics for the SOP generated with the few shot example

discuss if the generated output gets enhanced with the 
few shot input and if these enhancments add value (or not) to what was already there




