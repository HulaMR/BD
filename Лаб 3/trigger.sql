CREATE TABLE "user"(
"user_id" serial PRIMARY KEY,
"user_name" text,
"user_exp" int
);

CREATE TABLE "user_log"(
"id" serial PRIMARY KEY,
"user_log_id" int,
"user_log_name" text
);

INSERT INTO "user"("user_name", "user_exp")
VALUES ('worker1' , '1'), ('worker2', '2'), ('worker3', '3'), ('worker4', '4'),
('worker5', '5'), ('worker6', '6'), ('worker7', '7'), ('worker8', '8'), 
('worker9', '9'), ('worker10', '10') ;




CREATE OR REPLACE FUNCTION after_update_insert_func() RETURNS TRIGGER as $trigger$
DECLARE
	
BEGIN
	IF old."user_exp" >= 3 THEN
		RAISE NOTICE 'user_exp >= 3';
		INSERT INTO "user_log"("user_log_id", "user_log_name") VALUES (old."user_id", new."user_name");
		UPDATE "user_log" SET "user_log_name" = "user_log_name" || '_pro' ;
		RETURN NEW;
	END IF;

 	IF old."user_exp" < 3 THEN 
		RAISE NOTICE 'user_exp < 3';
		INSERT INTO "user_log"("user_log_id", "user_log_name") VALUES (old."user_id", new."user_name");
		UPDATE "user_log" SET "user_log_name" = "user_log_name" || '_tyro' ;	
		RETURN NEW;
	END IF;

	IF new."user_exp" >= 3 THEN
		RAISE NOTICE 'user_exp >= 3';
		INSERT INTO "user_log"("user_log_id", "user_log_name") VALUES (new."user_id", new."user_name");
		UPDATE "user_log" SET "user_log_name" = "user_log_name" || '_pro' ;
		RETURN NEW;
	END IF;

 	IF new."user_exp" < 3 THEN 
		RAISE NOTICE 'user_exp < 3';
		INSERT INTO "user_log"("user_log_id", "user_log_name") VALUES (new."user_id", new."user_name");
		UPDATE "user_log" SET "user_log_name" = "user_log_name" || '_tyro' ;	
		RETURN NEW;
	END IF;


END;
$trigger$ LANGUAGE plpgsql;

CREATE TRIGGER "after_update_insert_trigger"
AFTER UPDATE OR INSERT ON "user"
FOR EACH ROW
EXECUTE procedure after_update_insert_func(); 




UPDATE "user" SET "user_name" = "user_name" || '_t' WHERE "user_exp" = 2;
INSERT INTO "user"("user_name", "user_exp") VALUES ('worker11', '11') ;

