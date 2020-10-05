/*Please add ; after each select statement*/
CREATE PROCEDURE projectList()
BEGIN
	select project_name,team_lead,sum(income) income
     from Projects
    group by project_name,team_lead,internal_id order by internal_id;
END
