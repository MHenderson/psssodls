home=/home/matthew
savile_row_jar=$(home)/bin/savilerow-1.0RC1/savilerow.jar
minion_bin=$(home)/bin/minion-0.15/bin/minion
psssodls_eprime=$(home)/workspace/psssodls/psssodls.eprime
psssodls_param=$(home)/workspace/psssodls/psssodls.param
sr=java -ea -jar $(savile_row_jar)

all: psssodls.param.minion

psssodls.param.minion: $(psssodls_eprime) $(psssodls_param) 
	$(sr) -in-eprime $(psssodls_eprime) -in-param $(psssodls_param)

