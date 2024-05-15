import { Label } from "@/components/base/label";
import { Input } from "@/components/base/input";
import { useQueryStepStore } from "@/stores/QueryCondition";

export default function StepSelect() {

    const {
        queryStartStep, setQueryStartStep,
        queryEndStep, setQueryEndStep,
    } = useQueryStepStore();


    const handleStepChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const filteredValue = e.target.value.replace(/\D/g, '');
        if (e.target.id === 'startStep') setQueryStartStep(Number(filteredValue));
        else if (e.target.id === 'endStep') setQueryEndStep(Number(filteredValue));
    };

    function StepInputAlert() {
        if (queryStartStep - queryEndStep > 0) return <p className="ml-auto text-sm text-red-500">시작 스텝이 종료 스텝보다 큽니다.</p>
        return <p className="ml-auto text-sm text-white">null</p>
    };

    return (
        <div className="h-full flex flex-col gap-2 justify-center">
            <div className="flex flex-row gap-3">
                <div className="w-full">
                    <Label>시작 스텝</Label>
                    <Input id="startStep" type="number" min={0} value={queryStartStep} onChange={handleStepChange} />
                </div>
                <div className="w-full">
                    <Label>종료 스텝</Label>
                    <Input id="endStep" type="number" min={0} value={queryEndStep} onChange={handleStepChange} />
                </div>
            </div>
            <StepInputAlert />
        </div>
    )
}