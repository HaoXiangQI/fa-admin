-- upgrade --
ALTER TABLE `prod_edition` ADD `setter` VARCHAR(59) NOT NULL;
-- downgrade --
ALTER TABLE `prod_edition` DROP COLUMN `setter`;
