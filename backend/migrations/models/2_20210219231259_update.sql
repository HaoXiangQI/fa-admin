-- upgrade --
ALTER TABLE `prod_edition` DROP COLUMN `setter`;
-- downgrade --
ALTER TABLE `prod_edition` ADD `setter` VARCHAR(59) NOT NULL;
