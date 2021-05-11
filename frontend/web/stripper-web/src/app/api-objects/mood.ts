import MoodManipulator from "./mood-manipulator";

export default interface Mood{
    uuid:string,
    name:number,
    manipulators:MoodManipulator[]
}