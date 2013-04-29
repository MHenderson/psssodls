home=/home/matthew
savile_row_jar=$(home)/bin/savilerow-1.0RC1/savilerow.jar
minion_bin=$(home)/bin/minion-0.15/bin/minion
psssodls_eprime=$(home)/workspace/psssodls/psssodls.eprime
psssodls_param=$(home)/workspace/psssodls/psssodls.param
psssodls_param_minion=$(home)/workspace/psssodls/psssodls.param.minion
psssodls_param_solution=$(home)/workspace/psssodls/psssodls.param.solution
sr=java -ea -jar $(savile_row_jar)
sr_solve=$(sr) -m $(minion_bin)

.PHONY: clean minion solve

minion: $(psssodls_param_minion)
solve: $(psssodls_param_solution)

$(psssodls_param_minion): $(psssodls_eprime) $(psssodls_param) 
	$(sr) -in-eprime $(psssodls_eprime) -in-param $(psssodls_param) 

$(psssodls_param_solution): $(psssodls_eprime) $(psssodls_param) 
	$(sr_solve) -in-eprime $(psssodls_eprime) -in-param $(psssodls_param) 

clean:
	rm -f $(psssodls_param_minion)
	rm -f $(psssodls_param_solution)

