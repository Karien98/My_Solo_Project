-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema solo_project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema solo_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `solo_project` DEFAULT CHARACTER SET utf8 ;
USE `solo_project` ;

-- -----------------------------------------------------
-- Table `solo_project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `solo_project`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `solo_project`.`uploads`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `solo_project`.`uploads` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `photograph_title` VARCHAR(255) NULL,
  `photographer_username` VARCHAR(45) NULL,
  `photograph_description` VARCHAR(255) NULL,
  `location` VARCHAR(255) NULL,
  `photo_type` VARCHAR(45) NULL,
  `subject` VARCHAR(45) NULL,
  `shutter_speed` INT NULL,
  `aperture` INT NULL,
  `iso` INT NULL,
  `focal_lenght` INT NULL,
  `lighting_condition` VARCHAR(45) NULL,
  `time_of_day` DATETIME NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_uploads_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_uploads_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `solo_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
