-- upgrade --
ALTER TABLE `event` ADD `datetime` DATETIME(6);
-- downgrade --
ALTER TABLE `event` DROP COLUMN `datetime`;
