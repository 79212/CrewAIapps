# BI Article

### intro

bi should gives info and insight 

partly templates for a standard format, partly not so that changes in the data can be analysed 


what can ai do for us, Summarize data, comment on it, provide insights, draw charts

### summarization and charts

a simple example of a csv with summary and chart

running code is potentially a problem due to arbitrary code generation, so it either needs to be checked by a human or run in isolation. autogen give you the choice but crewai opts for safety and all code is run in a Docker container

we can get crewai to Summarize and draw a chart 

example here

but we will not necessarily get the same chart each time unless we tell the llm exactly what to do, in which case we might as well code it ourselves

example of ai summary and hand coded chart, here

### report

we probably  want to present a report in a format that is expected, consistency, expectation, etc

so create a template that structures the report but allows for creativity in sections for  insights , recommendations and so on 

example of template with agent to read the data and complete the report