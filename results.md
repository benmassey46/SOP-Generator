
## Results

Rank order each model from each provider on their text generation ability

e.g. 
- gpt-4o (best?)
- gpt-4-turbo
- gpt-4 (worst?)

Do the same for gemini and claude. 
probably need some literature/provider links to support this ranking assertion

- select 2 or 3 SOP types
- for each SOP type
  - generate SOP using a pair of models*
  - auto calculate review metrics for each model pair
  - auto calculate difference metrics for each model pair
  - auto calculate structure and content differences 

*pair of models - compare the top most ranked 
and then between the top most ranked and worst ranked
the idea being to show the best SOP generation possible 
and any gap between best and worst for the 
SOP generation task 

- Could also do multiple runs with the same model pairs 
and see if the metrics significantly difference
- Discuss the metrics, do they align when comparing the best models, are they significantly different when comparing 
best to worse ranked models in and across providers?

Could also do some manual checking to see if anything doesn't make sense
i.e. did the model wander off topic or make syntax/format errors in the output

-----------------------------------
Additional:
- Feed the expert file example text into the few shot example input window and generate SOP for the best models (and maybe worse models)  
- calculate diff, review and structure metrics for the SOP generated with the few shot example input against without few shot example input
- discuss if the generated output gets enhanced (or not) with the few shot input and if these enhancments add value (or not) gained when the expert doc was present in the SOP generation process 




